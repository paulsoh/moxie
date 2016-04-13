from ideas.views import IdeaListView
from ideas.models import Idea, Category


class CategoryListView(IdeaListView):

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        category = self.kwargs['slug']
        context['ideas'] = Idea.objects.filter(category__name__exact=category)
        return context
