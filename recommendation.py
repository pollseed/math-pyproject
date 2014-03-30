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

    return r

print('---------------')
print('ユークリッド距離 |')
print('---------------')
print('Lisa Rose : ')
print('{0:20} ==> {1}'.format('--- Gene Seymour', sim_distance(critics, 'Lisa Rose', 'Gene Seymour')))
print('{0:20} ==> {1}'.format('--- Toby', sim_distance(critics, 'Lisa Rose', 'Toby')))
print('{0:20} ==> {1}'.format('--- Jack Matthews', sim_distance(critics, 'Lisa Rose', 'Jack Matthews')))
print('{0:20} ==> {1}'.format('--- Michael Phillips', sim_distance(critics, 'Lisa Rose', 'Michael Phillips')))
print('{0:20} ==> {1}'.format('--- Mick LaSalle', sim_distance(critics, 'Lisa Rose', 'Mick LaSalle')))
print('{0:20} ==> {1}'.format('--- Claudia Puig', sim_distance(critics, 'Lisa Rose', 'Claudia Puig')))
print('------------')
print('ピアソン相関 |')
print('------------')
print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))