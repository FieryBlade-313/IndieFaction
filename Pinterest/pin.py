from py3pin.Pinterest import Pinterest
import json

pinterest = Pinterest(email='your-email',
                      password='your-password',
                      username='your-username',
                      cred_root='.')


def search(max_items=100, scope='pins', query='food'):
    print('Fetching')
    # After change in pinterest API, you can no longer search for users
    # Instead you need to search for something else and extract the user data from there.
    # current pinterest scopes are: pins, buyable_pins, my_pins, videos, boards
    results = []
    p = 0
    query = query + ' fanart'
    search_batch = pinterest.search(scope=scope, query=query)
    while len(search_batch) > 0:
        # print(search_batch)
        # input()
        for s in search_batch:
            # print(json.dumps(s, indent=4))
            # input()
            if 'objects' in s:
                for x in s['objects']:
                    if 'images' in x:
                        results.append(x['images']['orig'])
                        p += 1
                        if p >= max_items:
                            return results
                # results += [x['images']['orig']
                            # for x in s['objects'] if 'images' in x]
                # p += 1
                # if p >= max_items:
                #     return results
            elif 'images' in s:
                results.append(s['images']['orig'])
                p += 1
                if p >= max_items:
                    return results
        search_batch = pinterest.search(scope=scope, query=query)
    return results


res = search(max_items=100, query='spiderman')

for r in res:
    print(r)

print('\nTotal : '+str(len(res)))
