from django.db import connection


class QueryCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        query_count = len(connection.queries)
        print(f"Total database queries: {query_count}")
        # Добавьте в заголовки ответа (опционально)
        response['X-Query-Count'] = str(query_count)
        return response
