from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from question.models import Question, Alternative
from question.forms import RegisterQuestion
from accounts.models import Usuario
from django.http import JsonResponse
from random import shuffle


def dinamica(request):

    if request.method == 'GET':
        
        questions = list(Question.objects.all())

        # Embaralhar as perguntas
        shuffle(questions)

        # Para cada pergunta, obter suas alternativas
        questions_with_alternatives = []
        for question in questions:
            alternatives = Alternative.objects.filter(question=question)
            questions_with_alternatives.append({'question': question, 'alternatives': alternatives})

        context = {
            'questions_with_alternatives': questions_with_alternatives
        }

        return render(request, 'question/dinamica.html', context=context)



@login_required
def createQuestion(request):

    form = RegisterQuestion()

    if request.method == 'POST': 

        form = RegisterQuestion(request.POST)
        answer = request.POST.get("is_answer")

        if form.is_valid() and answer:
            question = form.save(commit=False)
            question.image = request.FILES.get("image")
            question.owner = Usuario.objects.get(pk=request.user.id)
            question.save()

            for posicao, alternativa in enumerate(request.POST.getlist("alternativa"), start=0):
                is_answer_bool = int(answer) == posicao
                if alternativa == '': continue 
                Alternative.objects.create(
                    text=alternativa,
                    question=question,
                    isAnswer=is_answer_bool
                )

                print(f"Posição: {posicao}, Alternativa: {alternativa}")

            return redirect("/question/list/")

    context = {
        'form': form
    }

    return render(request, 'question/create.html', context=context)


@login_required
def editQuestion(request, id):
    question = Question.objects.get(pk=id)
    form = RegisterQuestion(instance=question)

    if request.method == 'POST': 

        form = RegisterQuestion(request.POST, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            question.image = request.FILES.get("image")
            question.owner = Usuario.objects.get(pk=request.user.id)
            question.save()
            return redirect("/question/list/")
    
    context = {
        'form': form
    }

    return render(request, 'question/edit.html',context=context)


# alterar aqui depois
def viewQuestion(request, id):
    question = Question.objects.get(pk=id)
    alternatives = Alternative.objects.filter(question=question)
    context = {
        'question': question,
        'alternatives': alternatives
    }
    return render(request, 'question/view.html', context=context)

@login_required
def deleteQuestion(request, id):
    question = Question.objects.get(pk=id)

    if request.user.id == question.owner.id:
        question.delete()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def listQuestions(request):

    context = {
        'questions': Question.objects.filter(owner=Usuario.objects.get(pk=request.user.id))
    }

    return render(request, 'question/list.html',context=context)


def listAllQuestion(request):

    context = {
        'questions': Question.objects.all()
    }

    return render(request, 'question/listAll.html',context=context)

