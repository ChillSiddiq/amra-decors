import os

class VercelSpeedInsightsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if os.environ.get("VERCEL"):
            if 'text/html' in response.get('Content-Type', ''):
                response['Server-Timing'] = 'vercel;desc="Edge Function"'

        return response
