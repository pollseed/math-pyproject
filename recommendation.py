# coding:utf-8

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener':4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 3.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'You, Me and Dupree': 1.0,
        'Superman Returns': 4.0,
    }
}

from math import sqrt
import numpy as np

# ユークリッド距離
def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    # 比較がないなら0を返す.
    if len(si)==0: return 0

    # 全ての差の平方を足す.
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sum_of_squares)

# ピアソン相関関係を返す.
def sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    # 要素の数
    n=len(si)

    if n==0: return 0

    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    pSum=sum([prefs[p1][it] for it in si])

    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return np.abs(r)

# person以外の全ユーザの評点の重み付き平均を使い、personへの推薦を算出する.
def getRecommendations(prefs, person, similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:

        # 自分とは比較しない.
        if other == person:
            continue
        sim = similarity(prefs, person, other)

        # 0以下のスコアをスキップ
        if sim <= 0:
            continue

        for item in prefs[other]:

            # まだ見てない映画の得点のみを算出
            if item not in prefs[person] or prefs[person][item] == 0:

                # 類似度 * score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                # 類似度を合計
                simSums.setdefault(item, 0)
                simSums[item] += sim

        # 正規化したリストを作る
        rankings = [(total/simSums[item], item) for item, total in totals.items()]

        # ソート済みのリストを返す
        rankings.sort()
        rankings.reverse()
        return rankings if rankings.__len__() > 0 else '空'

# 指定のログを出力する形式
# @name 対象物
# @arithmetic 算術式
def println (name, arithmetic):
    print('{0:20} ==> {1}'.format(name, arithmetic))

# ユークリッド距離を実行します.
def doSim_distance(target, compared):
    println('--- {0}'.format(compared), sim_distance(critics, target, compared))

# 推薦を実行します.
def doGetRecommendations(name):
    println(name, getRecommendations(critics, name))

print('---------------')
print('ユークリッド距離 |')
print('---------------')
print('Lisa Rose : ')
doSim_distance('Lisa Rose', 'Gene Seymour')
doSim_distance('Lisa Rose', 'Toby')
doSim_distance('Lisa Rose', 'Jack Matthews')
doSim_distance('Lisa Rose', 'Michael Phillips')
doSim_distance('Lisa Rose', 'Mick LaSalle')
doSim_distance('Lisa Rose', 'Claudia Puig')
print('------------')
print('ピアソン相関 |')
print('------------')
println('Gene Seymour', sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
print('----')
print('推薦|')
print('----')
doGetRecommendations('Toby')
doGetRecommendations('Gene Seymour')
doGetRecommendations('Jack Matthews')
doGetRecommendations('Michael Phillips')
doGetRecommendations('Mick LaSalle')
doGetRecommendations('Claudia Puig')
doGetRecommendations('Lisa Rose')
