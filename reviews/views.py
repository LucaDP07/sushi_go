from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Testimonial
from django.urls import reverse_lazy
from .forms import TestimonialForm


class Testimonials(generic.ListView):
    """ This view is used to display all reviews """
    model = Testimonial
    template_name = 'reviews/testimonials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plain_message'] = True
        return context


class AddTestimonial(
        LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):

    """This view is used to allow a user to add a review"""
    form_class = TestimonialForm
    template_name = 'reviews/add_review.html'
    success_message = "Your review was added successfully"

    def form_valid(self, form):
        """
        Override the form_valid() method in model form view
        in order to set the signed in user as the name on the testimonial.
        """
        form.instance.name = self.request.user
        return super().form_valid(form)


class EditTestimonial(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, generic.UpdateView):

    """
    This view is used to allow logged in users to edit their own reviews
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'reviews/edit_review.html'
    success_message = "Review edited successfully"

    def test_func(self):
        """
        Prevent another user from editing user's review
        """
        testimonial = self.get_object()
        return testimonial.name == self.request.user\
            or self.request.user.is_superuser


class DeleteTestimonial(
        LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This view is used to allow logged in users to delete their own reviews
    """
    model = Testimonial
    template_name = 'reviews/delete_review.html'
    success_message = "Review successfully deleted"
    success_url = reverse_lazy('testimonials')

    def test_func(self):
        """
        Prevent another user from deleting another user's review
        """
        testimonial = self.get_object()
        return testimonial.name == self.request.user\
            or self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        SucessMessageMixin cannot be used in generic.DeleteView.

        """
        messages.success(self.request, self.success_message)
        return super(DeleteTestimonial, self).delete(request, *args, **kwargs)
