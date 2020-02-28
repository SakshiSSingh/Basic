def height(root):
    if root is None:
        return 0

    elif root.left or root.right:
        left_d = height(root.left)
        right_d = height(root.right)

        if left_d > right_d:
            return left_d + 1
        else:
            return right_d + 1

    else:
        return 0
