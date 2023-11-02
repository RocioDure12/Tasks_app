from fastapi import APIRouter
from ..controllers.users_controller import UsersController

router = APIRouter(
    prefix='/tasks'
)

controller=UsersController()

router.add_api_route('/', controller.create, methods=['POST'])
router.add_api_route('/', controller.read, methods=['GET'])
router.add_api_route('/', controller.update, methods=['PUT'])
router.add_api_route('/', controller.delete, methods=['DELETE'])