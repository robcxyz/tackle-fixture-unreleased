from tackle import BaseHook, Field


class UnreleasedFixtureHook(BaseHook):
    """A fixture."""

    hook_name: str = 'unreleased'
    src: str = Field(..., description="A fixture source.")
    args: list = ['src']

    def exec(self) -> str:
        return self.src
