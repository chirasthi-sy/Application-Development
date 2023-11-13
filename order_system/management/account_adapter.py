from allauth.account.adapter import DefaultAccountAdapter
class NoNewUserAccountAdapter(DefaultAccountAdapter)
    def is_open_for_signup(selfself,request):
        return False