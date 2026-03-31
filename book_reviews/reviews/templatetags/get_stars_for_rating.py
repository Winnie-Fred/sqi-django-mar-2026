from django import template

register = template.Library()

@register.simple_tag
def get_rating_stars(rating: int):
    shaded_star = "★"
    unshaded_star = "☆"
    rating = max(0, min(rating, 5))
    no_of_shaded_stars = rating
    MAX_RATING = 5
    
    no_of_unshaded_stars = MAX_RATING - rating

    return f"{no_of_shaded_stars * shaded_star}{no_of_unshaded_stars * unshaded_star}"


print(get_rating_stars(-6))