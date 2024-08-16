REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # "DEFAULT_FILTER_BACKENDS": [
    #     "django_filters.rest_framework.DjangoFilterBackend",
    #     "rest_framework.filters.SearchFilter",
    #     "rest_framework.filters.OrderingFilter",
    # ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    # "PAGE_SIZE": 12,
    # "SEARCH_PARAM": "q",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "120/minute",
        "user": "240/minute",
        "testing": "2/minute",
    },
}
