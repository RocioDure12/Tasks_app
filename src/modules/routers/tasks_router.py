from fastapi import APIRouter, Response
from ..controllers.tasks_controller import TasksController
from ..models.task import Task
from typing import List

router = APIRouter(
    prefix='/tasks'
)

controller = TasksController()

router.add_api_route('/', controller.create, methods=['POST'])
router.add_api_route('/', controller.read, methods=['GET'])
router.add_api_route('/{id}', controller.update, methods=['PUT'])
router.add_api_route('/{id}', controller.delete, methods=['DELETE'])
