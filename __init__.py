from pathlib import Path
from typing import List

from api.models.Page import Page
from core.lib.quick_lint import lint_project
from core.tech_stacks import TechStack
from core.tech_stacks.ai_parse_pages import ai_parse_pages
from core.tech_stacks.build_generic import run_build
from core.types import CodeDict

tech_stack_dir = Path(__file__).parent


with open(Path(__file__).parent / "example_usage.md") as f:
    example_usage_content = f.read()

tech_stack_dir = Path(__file__).parent


class ShadcnTemplateTechStack(TechStack):
    def __init__(self):
        super().__init__(
            version="1.0.0",
            name=tech_stack_dir.name,
            build_function=lambda project_dir: run_build(
                project_dir, template_path=tech_stack_dir / "template"
            ),
            lint_function=lint_project,
            components={
                "FILE_TO_UPDATE": "src/App.jsx",
                "FILE_CONTENT": 'code("src/App.jsx")',
                "TECH_STACK_SUMMARY": "React with shadcn-ui and Tailwind CSS",
                "TECH_STACK_POINTS": """
- Vite
- React
- shadcn-ui
- Tailwind CSS
""".strip(),
                "TECH_STACK_INSTRUCTIONS": f"""
- Remember spacing between components, such as using ml-2 or mr-2 / space-x-2 etc..
- Use shadcn-ui components from @/components/ui/[component-name] whenever possible. Reference for usage:
{example_usage_content}""".strip(),
            },
            default_init_file="src/App.jsx",
        )

    async def parse_pages(self, code: CodeDict) -> List[Page]:
        pages = await ai_parse_pages(code["src/App.jsx"])
        return pages
