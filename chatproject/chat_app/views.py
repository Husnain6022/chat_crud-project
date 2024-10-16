from django.shortcuts import render, redirect
from rest_framework_simplejwt.tokens import AccessToken
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect
from rest_framework_simplejwt.tokens import AccessToken
from django.http import HttpResponseForbidden

def chat_view(request, room_name):
    # Get token from the query string
    token = request.GET.get('token')

    # If no token is found, redirect to the sign-in page
    if not token:
        return redirect('/api/auth/template/signin/')

    try:
        # Validate the token
        access_token = AccessToken(token)
        user_id = access_token['user_id']  # Extract user_id from the token

        # Render the chat room page, passing the user_id to the template
        return render(request, 'chat.html', {
            'room_name': room_name,
            'access_token': token,  # Pass the token to the template for WebSocket use
            'user_id': user_id  # Pass the user_id to the template
        })
    except Exception as e:
        print(f"Token validation error: {e}")
        return HttpResponseForbidden("Invalid or expired token. Please sign in again.")
