from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):

    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 100