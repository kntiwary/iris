__author__ = 'kamta'

from app.main.util.helper import get_dataframe


def iris_stats(url=None):
    df = get_dataframe(url)
    maxvals, minvals, meanvals, countvals = {}, {}, {}, {}
    try:
        for key, val in df.max().iteritems():
            maxvals[key] = val
        for key, val in df.min().iteritems():
            minvals[key] = val
        for key, val in df.mean().iteritems():
            meanvals[key] = val
        for key, val in df.count().iteritems():
            countvals[key] = val

        response_stats = {'counts': countvals,
                          'maxvals': maxvals,
                          'minvals': minvals,
                          'meanval': meanvals,
                          'message': 'Iris detailed stats'}
    except Exception as e:
        print(e)
        response_stats = {'message': e}

    return response_stats


def sepcies_maxlength(maxlength, url=None):
    # maxlength = int(maxlength)
    try:
        df = get_dataframe(url)
        species = df[df['sepal_length'] <= maxlength]
        out = species.groupby('species').count()['sepal_length']
        species_cnt = {}
        for key, val in out.items():
            species_cnt[key] = val
        response_cnt = {f'species_count at length {maxlength}': species_cnt}
    except Exception as e:
        # print(e)
        response_cnt = {'message': e}
    return response_cnt
