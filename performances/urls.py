from django.urls import path
from . import views

urlpatterns = [
    path('performanceindicator/',views.performanceindicatorView.as_view(),name='performanceindicator'),
    path('performance/',views.performanceView.as_view(),name='performance'),
    path('performanceappraisal/',views.performanceappraisalView.as_view(),name='performanceappraisal'),
    path('performanceindicator/',views.performanceIndicatorView.as_view(),name='performanceindicator'),
# ----------------------------------------Goal Tracking-------------------------------------------------------
    
    path('goaltracking/',views.GoalTrackingCreateView.as_view(),name='goaltracking'),
    path('goaltracking_remove/<int:id>',views.GoalTrackingRemove.as_view(),name='goaltracking_remove'),

# ----------------------------------------/Goal Tracking-------------------------------------------------------
# ----------------------------------------Goal Type-------------------------------------------------------
    
    path('goaltype/',views.GoalTypeCreateView.as_view(),name='goaltype'),
    # path('goaltype_list/',views.GoalTypeListView.as_view(),name='goaltype_list'),
    path('goaltype_manage/<int:pk>',views.GoalTypeManage.as_view(),name='goaltype_manage'),
    path('goaltype_remove/<int:id>',views.GoalTypeRemove.as_view(),name='goaltype_remove'),

# ----------------------------------------/Goal Type-------------------------------------------------------

    
# ----------------------------------------Training-------------------------------------------------------
    path('trainings/',views.TrainingCreateView.as_view(),name='trainings' ),
    path('training_manage/<int:id>',views.GoalTrackingManage.as_view(),name='training_manage'),
    path('training_remove/<int:id>',views.TrainingRemove.as_view(),name='training_remove'),
# ----------------------------------------Training-------------------------------------------------------
# ----------------------------------------Trainer------------------------------------------------------- 

    path('trainers/',views.TrainersCreateView.as_view(),name='trainers'),
    # path('trainer_list/',views.TrainersListView.as_view(),name='trainer_list'),
  
    path('trainer_manage/<int:pk>',views.TrainerManage.as_view(),name='trainer_manage'),
    path('trainer_remove/<int:id>',views.TrainerRemove.as_view(),name='trainer_remove'),
    
# ----------------------------------------/Trainer-------------------------------------------------------
# ----------------------------------------Training Type ------------------------------------------------------------

    path('training_type/',views.TrainingTypeCreateView.as_view(),name='training_type'),
    # path('training_type_list/',views.TrainingTypeListView.as_view(),name='training_type_list'),
    path('training_type_manage/<int:pk>',views.TrainingTypeManage.as_view(),name='training_type_manage'),
    path('training_type_remove/<int:id>',views.TrainingTypeRemove.as_view(),name='training_type_remove'),
    

# ----------------------------------------/Training Type ------------------------------------------------------------
    path('promotion/',views.promotionView.as_view(),name='promotion'),
    path('resignation/',views.resignationView.as_view(),name='resignation'),

# ---------------------------------------- Termination ------------------------------------------------------------
   
    path('termination/',views.TerminationCreate.as_view(),name='termination'),
    path('termination_remove/<int:id>',views.TerminationRemove.as_view(),name='termination_remove'),

# ---------------------------------------- /Termination ------------------------------------------------------------
   
]