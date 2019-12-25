from django.urls import path
import marketing.views

urlpatterns = [
  path('cluster/kmeans/', marketing.views.KmeansView.as_view()),
  path('swot/', marketing.views.swot),
  path('stp/', marketing.views.stp),
  path('retaintionRate/', marketing.views.retaintionRate),
  path('survivalRate/', marketing.views.survivalRate),
  path('cluster/decisionTree/', marketing.views.DecisionTreeView.as_view()),
]
