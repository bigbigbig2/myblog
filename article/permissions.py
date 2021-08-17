#权限控制文件
#任何人都可以查看资源；但是新增（CREATE）、更新（PUT）、删除（DELETE）等修改操作就只允许管理员执行。
from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """

    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD or OPTIONS 请求.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 仅管理员可进行其他操作
        return request.user.is_superuser
