from fastapi import APIRouter
from database import tasks_db

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/")
async def get_tasks_stats() -> dict:
    by_quadrant = {quadrant: 0 for quadrant in ["Q1", "Q2", "Q3", "Q4"]}
    completed = 0

    for task in tasks_db:
        by_quadrant[task["quadrant"]] += 1
        if task["completed"]:
            completed += 1

    return {
        "total_tasks": len(tasks_db),
        "by_quadrant": by_quadrant,
        "by_status": {
            "completed": completed,
            "pending": len(tasks_db) - completed
        }
    }
