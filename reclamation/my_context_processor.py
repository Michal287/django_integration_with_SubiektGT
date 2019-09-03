from django.contrib.auth.models import User

from .models import Company, Branch


def company_request(request):

    if hasattr(request, 'user'):
        current_user = Company.objects.get(basic_info_id=User.objects.get(username=request.user).id)
        branches = Branch.objects.filter(company_id=current_user.id)
        return {"branches": branches}

    return {}