import json
from pydoc import text
from django.http import HttpResponse
from .forms import prompt_form
from django.shortcuts import redirect, render
from .models import chat, message
from django.contrib.auth.decorators import login_required
import google.generativeai as genAI
from django.conf import settings
from . import services

genAI.configure(api_key=settings.GOOGLE_API_KEY)


@login_required
def new_chat_view(request):
    user = request.user
    user_chats = chat.objects.filter(user=user)

    if request.method == "POST":
        form = prompt_form(request.POST)
        if form.is_valid():

            response = services.generate_response(request.POST["text"])

            aiResponseInJSON = response

            new_chat = chat.objects.create(title=aiResponseInJSON, user=user)
            new_user_prompt_message = message.objects.create(
                text=request.POST["text"], chat=new_chat, isPrompt=True
            )
            new_ai_response_message = message.objects.create(
                text=aiResponseInJSON,
                chat=new_chat,
                isPrompt=False,
                hasMermaid=False,
                mermaid="",
            )

            return redirect(to=f"{user.id}/{new_chat.id}", permanent=True)
    else:
        form = prompt_form()
    return render(request, "chats/new_chat.html", {"form": form, "chats": user_chats})


@login_required
def chat_view(request, user_id, chat_id):
    current_chat = chat.objects.get(id=chat_id)
    messages = current_chat.message.all().order_by("id")
    user_chats = chat.objects.filter(user=user_id).values()

    if request.method == "POST":
        form = prompt_form(request.POST)
        if form.is_valid():

            response = services.generate_response(request.POST["text"])
            aiResponseInJSON = json.loads(
                response.replace("```json", "").replace("```", "")
            )

            new_user_prompt_message = message.objects.create(
                text=request.POST["text"], chat=current_chat, isPrompt=True
            )
            new_ai_response_message = message.objects.create(
                text=aiResponseInJSON["content"],
                chat=current_chat,
                isPrompt=False,
                hasMermaid=aiResponseInJSON["hasMermaid"],
                mermaid=aiResponseInJSON["mermaid"],
            )
        return redirect(to=f"/chats/{user_id}/{chat_id}")
    else:
        form = prompt_form()

    return render(
        request,
        "chats/chat.html",
        {
            "messages": messages,
            "form": form,
            "chats": user_chats,
            "current_chat": current_chat,
        },
    )
