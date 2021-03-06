from django.urls import path
import marketing.views

urlpatterns = [
  path('cluster/kmeans/', marketing.views.KmeansView.as_view()),
  path('swot/', marketing.views.swot),
  path('stp/', marketing.views.STPView.as_view()),
  path('retentionRate/', marketing.views.RetentionRateView.as_view()),
  path('survivalRate/', marketing.views.SurvivalRateView.as_view()),
  path('cluster/decisionTree/', marketing.views.DecisionTreeView.as_view()),
  path('rfm/', marketing.views.RFMView.as_view()),
]
