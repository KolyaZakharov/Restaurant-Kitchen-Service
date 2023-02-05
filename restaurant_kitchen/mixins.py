from django.views.generic import ListView
from restaurant_kitchen.forms import SearchForm

class SearchMixin(ListView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchMixin, self).get_context_data(
            object_list=object_list, **kwargs
        )

        name = self.request.GET.get("name", "")

        context["search_form"] = SearchForm(initial={"name": name},)

        return context

    def get_queryset(self):
        query_set = super().get_queryset()
        search_request = self.request.GET.get("name")
        if search_request:
            return query_set.filter(name__icontains=search_request)

        return query_set
