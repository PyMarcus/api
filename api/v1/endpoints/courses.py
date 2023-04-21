from typing import List, Any, Sequence
from fastapi import APIRouter, status, Depends, HTTPException, Response, Path
from sqlalchemy import Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import CourseModel
from schemas import CourseSchema
from core import get_session


router: APIRouter = APIRouter()


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=CourseSchema,
    description="Insert a course in the database",
    summary="Create a course"
)
async def post_course(
        course: CourseSchema,
        db: AsyncSession = Depends(get_session)  # dependencies injected
) -> CourseSchema:
    """
    Create a new course in the database
    :param course: CourseSchema (JSON)
    :param db: AsyncSession
    :return: CourseSchema (JSON)
    """
    new_course = CourseModel(
        title=course.title,
        lessons=course.lessons,
        hours=course.hours,
    )
    db.add(new_course)
    await db.commit()
    return new_course


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=List[CourseSchema],
    description="Get all courses from the database",
    summary="Get all courses"
)
async def get_courses(db: AsyncSession = Depends(get_session)) -> Sequence[Row | RowMapping | Any]:
    async with db as session:
        response = await session.execute(select(CourseModel))
        return response.scalars().all()


@router.get(
    path='/{course_id}',
    status_code=status.HTTP_200_OK,
    response_model=CourseSchema,
    description="Get a course from the database",
    summary="Get only one course"
)
async def get_course(
            course_id: str = Path(
            title="Course ID",
            description="ID must be bigger than 0",
        ),
        db: AsyncSession = Depends(get_session),
) -> CourseSchema:
    async with db as session:
        response = await session.execute(select(CourseModel).filter(CourseModel.id == id))
        response = response.scalar_one_or_none()
        if response:
            return response
        raise HTTPException(
            detail="Course Not Found.",
            status_code=status.HTTP_404_NOT_FOUND
        )


@router.put(
    path='/{course_id}',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=CourseSchema,
    description="Update a course information",
    summary="Update course")
async def put_course(
            course: CourseSchema,
            course_id: str = Path(
            title="Course ID",
            description="ID must be bigger than 0",
        ),
        db: AsyncSession = Depends(get_session),
) -> CourseSchema:
    async with db as session:
        response = await session.execute(select(CourseModel).filter(CourseModel.id == id))
        response = response.scalar_one_or_none()
        if response:
            response.title = course.title
            response.lessons = course.lessons
            response.hours = course.hours
            await session.commit()
            return response
        raise HTTPException(
            detail="Course not exists.",
            status_code=status.HTTP_404_NOT_FOUND
        )


@router.delete(
    path='/{course_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete a course from database",
    summary="Delete course")
async def delete_course(
            course_id: str = Path(
            title="Course ID",
            description="ID must be bigger than 0",
        ),
        db: AsyncSession = Depends(get_session),
) -> None:
    async with db as session:
        response = await session.execute(select(CourseModel).filter(CourseModel.id == id))
        response = response.scalar_one_or_none()
        if response:
            await session.delete(response)
            await session.commit()
            return None
        raise HTTPException(
            detail="Course not exists.",
            status_code=status.HTTP_404_NOT_FOUND
        )
