from django.urls import path
from . import views

urlpatterns = [
    path('performanceindicator/',views.performanceindicatorView.as_view(),name='performanceindicator'),
    path('performance/',views.performanceView.as_view(),name='performance'),
    path('performanceappraisal/',views.performanceappraisalView.as_view(),name='performanceappraisal'),
    path('performanceindicator/',views.performanceIndicatorView.as_view(),name='performanceindicator'),
# ----------------------------------------Goal Tracking-------------------------------------------------------
    
    path('goaltracking/',views.GoalTrackingCreateView.as_view(),name='goaltracking'),
    # path('goaltracking_list/',views.GoalTrackingListView.as_view(),name='goaltracking_list'),
    # path('goaltracking_remove/<int:id>',views.GoalTrackingRemove.as_view(),name='goaltracking_remove'),

# ----------------------------------------/Goal Tracking-------------------------------------------------------
# ----------------------------------------Goal Type-------------------------------------------------------
    
    path('goaltype/',views.GoalTypeCreateView.as_view(),name='goaltype'),
    path('goaltype_list/',views.GoalTypeListView.as_view(),name='goaltype_list'),
    # path('goaltype_remove/<int:pk>/delete/',views.GoalTypeRemove.as_view(),name='goaltype_remove'),
    path('goaltype_remove/<int:id>',views.GoalTypeRemove.as_view(),name='goaltype_remove'),

# ----------------------------------------/Goal Type-------------------------------------------------------

    # path('trainings/',views.trainingsView.as_view(),name='trainings'),
    # path('trainers/',views.trainersView.as_view(),name='trainers'),
    # path('goaltracking/',views.goalTrackingView.as_view(),name='goaltracking'),
    # path('goaltype/',views.goalTypeCreateView.as_view(),name='goaltype'),

# ----------------------------------------Training-------------------------------------------------------
    path('trainings/',views.TrainingCreateView,name='trainings'),
   
    path('training_remove/<int:id>',views.TrainingRemove.as_view(),name='training_remove'),
# ----------------------------------------Training-------------------------------------------------------
# ----------------------------------------Trainer------------------------------------------------------- 

    path('trainers/',views.TrainersCreateView.as_view(),name='trainers'),
    path('trainer_list/',views.TrainersListView.as_view(),name='trainer_list'),
  
    path('trainer_remove/<int:id>',views.TrainerRemove.as_view(),name='trainer_remove'),
    
# ----------------------------------------/Trainer-------------------------------------------------------
# ----------------------------------------Training Type ------------------------------------------------------------

    path('training_type/',views.TrainingTypeCreateView.as_view(),name='training_type'),
    path('training_type_list/',views.TrainingTypeListView.as_view(),name='training_type_list'),
    # path('training_type_remove/<int:id>/delete/',views.TrainingTypeRemove.as_view(),name='training_type_remove'),
    path('training_type_remove/<int:id>',views.TrainingTypeRemove.as_view(),name='training_type_remove'),
    

# ----------------------------------------/Training Type ------------------------------------------------------------
    path('promotion/',views.promotionView.as_view(),name='promotion'),
    path('resignation/',views.resignationView.as_view(),name='resignation'),
    path('termination/',views.terminationView.as_view(),name='termination'),
   
]