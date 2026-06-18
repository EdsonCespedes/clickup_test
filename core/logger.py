import sys
import structlog

def setup_logging() -> None:
    """
    Configure structlog to provide structured logging
    that is readable in both local consoles and CI environments.
    """
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(
                fmt="%Y-%m-%d %H:%M:%S",
                utc=True,
            ),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            (
                structlog.dev.ConsoleRenderer()
                if sys.platform == "win32"
                else structlog.processors.JSONRenderer()
            ),
        ],
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(10),
        cache_logger_on_first_use=True,
    )

logger = structlog.get_logger()