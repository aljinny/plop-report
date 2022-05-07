from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from mainpage import db
from mainpage.models import Question, bugs_pl
from mainpage.forms import QuestionForm, AnswerForm

import random
#from mainpage.views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/plop')


@bp.route('/manage/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/playlist/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    """
    lotto_l = []
    for i in range(1, 46):
        lotto_l.append(random.sample(list(range(1, 46)), 2))
    lotto = random.sample(lotto_l, 7)
    """

    song_list = bugs_pl.query.filter(bugs_pl.plop_id == question_id)
    song_list_count = bugs_pl.query.filter(bugs_pl.plop_id == question_id).count()
    #song_list = bugs_pl.query.join(Question).filter(Question.id == 3)
    #메인 호출
    ran = random.sample(list(range(1,song_list_count)),7)
    song_list_r = []
    for i, v in enumerate(song_list) :
        for r in ran :
            if (i==r) :
                song_list_r.append([v.s_title,v.s_artist])
    return render_template('question/layout.html', question=question, form=form, song_list_r=song_list_r)

#question_detail호출
@bp.route('/community/<int:question_id>/')
def community(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
#@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, colors=form.colors.data, colors_code=form.colors_code.data, img_url=form.img_url.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    #if Question.id

    return render_template('question/question_form.html', form=form)

@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
#@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    """
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    """
    if request.method == 'POST':  # POST 요청
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else:  # GET 요청
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form)

@bp.route('/delete/<int:question_id>')
#@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    """
    if g.user != question.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    """
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('question._list'))
