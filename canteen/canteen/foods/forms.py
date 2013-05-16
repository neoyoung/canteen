from django import forms
from canteen.foods.models import Food, FoodReview


class FoodAdminForm(forms.ModelForm):
    """
    ModelForm class to validate food instance
    data before saving from admin interface.
    """
    class Meta:
        model = Food


class FoodReviewForm(forms.ModelForm):
    """ Form class to submit a new ProductReview instance """
    class Meta:
        model = FoodReview
        exclude = ('user', 'food', 'is_approved')
