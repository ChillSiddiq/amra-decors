def get_category_choices(categories, level=0):
    choices = []
    indent = "— " * level
    for category in categories:
        choices.append((category.id, f"{indent}{category.name}"))
        children = category.children.all()
        if children.exists():
            choices += get_category_choices(children, level + 1)
    return choices