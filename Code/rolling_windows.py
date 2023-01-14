class rolling:
    def __init__(self):
        self.head = None
        
    def add_node(self, data):
        curr = self.head
        if curr is None:
            newNode = Node(data, self.head)
            self.head = newNode
            return True

        if curr.data['documentID'] > data['documentID']:
            newNode = Node(data, self.head)
            self.head = newNode
            return True

        while curr.nextNode is not None:
            if curr.nextNode.data['documentID'] > data['documentID']:
                break
            curr = curr.nextNode
        newNode = Node(data, curr.nextNode)
        curr.nextNode = newNode
        return True
    
    def get_head_ptr(self):
        return self.head
    
    def find_node(self):
        curr = self.head
        postings_list = []
        while curr is not None:
            posting = curr.data['documentID']
            postings_list.append(posting)
            curr = curr.nextNode
        return postings_list
    
    def find_skip_node(self):
        current = self.head
        skip_postings_list = []
        while current is not None:
            posting = current.data['documentID']
            skip_postings_list.append(posting)
            current = current.nextSkip
        return skip_postings_list

    def find_node_tfidf(self):
        curr = self.head
        postings_list = {}
        while curr is not None:
            postings_list[curr.data['documentID']] = curr.data['tf-idf']
            curr = curr.nextNode
        return postings_list
     
    def insertSkips(self, intervals):
        curr = self.head
        t = curr
        cnt = 0
        
        for i in range(intervals):
            while t and cnt < (i+1) * (intervals):  #traversing one by one until skip interval value
                cnt += 1
                t = t.nextNode
            curr.nextSkip = t
            curr = t

        return True
    
    def set_idf(self, corpus_size, doc_freq):
        temp = self.head
        while (temp):
            temp.data['tf-idf'] *= corpus_size / doc_freq
            temp = temp.nextNode

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.nextNode
            
    def print_skip_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.nextSkip
                

def DaatAND(pl1, pl2):
    res = new_LL()
    num_comps = 0
    
    if not pl1:
        return pl2
    if not pl2:
        return pl1
    
    while pl1 and pl2:
        if pl1.data["documentID"] < pl2.data["documentID"]:
            pl1 = pl1.nextNode
        elif pl2.data["documentID"] < pl1.data["documentID"]:
            pl2 = pl2.nextNode
        else:
            res.add_node(pl1.data)
            pl1 = pl1.nextNode
            pl2 = pl2.nextNode
        num_comps += 1
        
    return res, num_comps

def DaatANDwithSkip(pl1,pl2):
    res = new_LL()
    num_comps = 0
    
    if not pl1:
        return pl2
    if not pl2:
        return pl1
    
    while pl1 and pl2:
        if pl1.data["documentID"] != pl2.data["documentID"]:
            if pl1.data["documentID"] < pl2.data["documentID"]:
                if pl1.nextSkip:
                    if pl1.nextSkip.data["documentID"] < pl2.data["documentID"]:
                        pl1 = pl1.nextSkip
                    else:
                        pl1 = pl1.nextNode
                else:
                    pl1 = pl1.nextNode
            else:
                if pl2.nextSkip:
                    if pl2.nextSkip.data["documentID"] < pl1.data["documentID"]:
                        pl2 = pl2.nextSkip
                    else:
                        pl2 = pl2.nextNode
                else:
                    pl2 = pl2.nextNode
        else:
            res.add_node(pl1.data)
            pl1 = pl1.nextNode
            pl2 = pl2.nextNode
        
        num_comps += 1
        
    return res, num_comps

inverted_index = {}
for doc_id in indexing.keys():
    all_tokens = indexing[doc_id] # gives list of tokens pertaining to given docID
    term_dict_with_tf = get_term_tf_dict(all_tokens)

    for token in term_dict_with_tf:
        if token not in inverted_index:
            inverted_index[token] = {'documentFrequency': 1, 'postings_list': new_LL()}
            term_obj = inverted_index[token]
            tf_doc_id_node = {'tf-idf': (term_dict_with_tf[token]), "documentID" : int(doc_id)}
            term_obj['postings_list'].add_node(tf_doc_id_node)

        elif token in inverted_index and doc_id not in inverted_index[token]:
            term_obj = inverted_index[token]
            term_obj['documentFrequency'] += 1
            tf_doc_id_node = {'tf-idf': (term_dict_with_tf[token]), "documentID" : int(doc_id)}
            term_obj['postings_list'].add_node(tf_doc_id_node)
            
for term in inverted_index:
    doc_f = inverted_index[term]['documentFrequency']
    l_obj = inverted_index[term]['postings_list']
    l_obj.set_idf(len(indexing), doc_f)

def get_skip_attributes(term):
    df = inverted_index[term]['documentFrequency']
    if isPerfectSquare(df):
        no_of_skip_pointers = math.floor(math.sqrt(df)) - 1
    else:
        no_of_skip_pointers = math.floor(math.sqrt(df))
        
    length_between_skips = int(round(math.sqrt(df), 0))
    
    return no_of_skip_pointers, length_between_skips


def return_head_ptr(term):
    return inverted_index[term]['postings_list']

#q = open('Data//queries.json', encoding="utf8")
with open('queries.json') as f:
     staticQuery = json.load(f)
requestDataDict = None

@app.post('/execute_query')
def post_dict():
    global requestDataDict 
    requestDataDict = request.get_json()

    daatANDresults(list_of_term_postings, 1)
    daatANDresults(list_of_term_postings, 2)
    daatANDresults(list_of_term_postings, 3)
    return daatANDresults(list_of_term_postings, 4)


q = requestDataDict
if q:
    listOfQueries = q["queries"]
else:
    listOfQueries = staticQuery["queries"]
queries = []
og = []

#listOfQueries = q["queries"]

for line in listOfQueries:
    query = line
    og.append(query)
    query = query.replace('\n', '')
    queries.append(query) 

mod = []
for query in range(len(queries)):
    queryTobeIndexed = queries[query].lower()
    after_removing_special = re.sub(re.compile('\W'), ' ', queryTobeIndexed)
    remove_extra_whitespace = " ".join(after_removing_special.split())
    tokenize = remove_extra_whitespace.split(' ')
    stopword_remove = [item for item in tokenize if not item in stp_wrds]
    stemmed = [ps.stem(item) for item in stopword_remove]
    queries[query] = stemmed
    mod.append(stemmed)
    
mod = [' '.join(item) for item in mod]
mapping_dictionary = dict(zip(mod, og))
#print(mapping_dictionary) -> Maps the original query.


#### GET POSTINGLIST for each term in a query

def getPostingList(queries, invertedIndex):
    list_of_dictionaries = []
    for flat_list in queries:
        dictPost = {}
        for token in range(len(flat_list)):
            
            if invertedIndex[flat_list[token]]:
                postingListObj = invertedIndex[str(flat_list[token])]
                postingList = postingListObj['postings_list']
                
                if postingList:
                    postings_list = postingList.find_node()
                else:
                    postings_list = []

                dictPost[flat_list[token]] = postings_list
                   
        list_of_dictionaries.append(dictPost)
        
    return list_of_dictionaries


# list[0]: {'novel':PL, 'coronaviru':PL}
# List[1]: {'epidem':PL, 'pandem':PL}
d = {}
main_d = {}
list_of_all_queries = getPostingList(queries, inverted_index)
for item in list_of_all_queries:
    d.update(item)
main_d['postingsList'] = d
#print("\n")
#print(main_d)


def getSortedQueryTokenList(queries, invertedIndex):
    query_L = [] 
    for query in queries:
        query_token_list = []
        for term in query:
            if term in invertedIndex.keys():
                query_token_list.append(invertedIndex[term])
            else:
                query_token_list.append({'documentFrequency': 0, 'postings_list': None})

        query_L.append(query_token_list)

    return query_L


# list[0]: {'novel':{docFreq, PostingList}, 'coronaviru':{docFreq, PostingList}}
# list[1]: {'epidem':{docFreq, PostingList}, 'pandem':{docFreq, PostingList}}
list_of_term_postings = getSortedQueryTokenList(queries, inverted_index)

#print(list_of_term_postings[-1]) -> Before Sorting

for retrieved_posting in list_of_term_postings:
    for i in range(len(retrieved_posting) - 1):
        for j in range(i+1, len(retrieved_posting)):
            if retrieved_posting[i]['documentFrequency'] > retrieved_posting[j]['documentFrequency']:
                retrieved_posting[i], retrieved_posting[j] = retrieved_posting[j], retrieved_posting[i]

#print(list_of_term_postings[-1]) -> After Sorting

def getPostingListWithSkips(queries, invertedIndex):
    list_of_dictionaries = []
    for flat_list in queries:
        dictPost = {}
        for token in range(len(flat_list)): 
            
            if invertedIndex[flat_list[token]]:
                postingListObj = invertedIndex[str(flat_list[token])]
                postingList = postingListObj['postings_list']
                no_of_skips, length_btw_skips = get_skip_attributes(flat_list[token])
                postingList.insertSkips(length_btw_skips)
                
                if postingList:
                    postings_list = postingList.find_skip_node()
                else:
                    postings_list = []

                dictPost[flat_list[token]] = postings_list
                   
        list_of_dictionaries.append(dictPost)
        
    return list_of_dictionaries

# list[0]: {'novel':PL, 'coronaviru':PL}
# List[1]: {'epidem':PL, 'pandem':PL}
skipD = {}
listOfAllQueries = getPostingListWithSkips(queries, inverted_index)
for item in listOfAllQueries:
    skipD.update(item)
main_d['postingsListSkip'] = skipD

#### DAAT AND

def daatANDresults(termPostingsList, flag):
    if flag == 1:
        d = {}
        z = 0
        for query in termPostingsList:
            query_dict = {}
            total_comparisons = 0
            result_list = []
            for i in range(len(query) - 1):
                h1 = query[i]['postings_list'].get_head_ptr()
                h2 = query[i + 1]['postings_list'].get_head_ptr()
                result, comps = DaatAND(h1, h2)
                result_list = result.find_node()
                total_comparisons += comps
            query_dict['num_comparisons'] = total_comparisons
            query_dict['num_docs'] = len(result_list)
            query_dict['results'] = result_list
            
            d[og[z]] = query_dict
            z += 1
        main_d["daatAnd"] = d 

    elif flag == 2:
        d = {}
        z = 0
        for query in list_of_term_postings:
            query_dict = {}
            total_comparisons = 0
            result_list = []
            for i in range(len(query) - 1):
                h1 = query[i]['postings_list'].get_head_ptr()
                h2 = query[i + 1]['postings_list'].get_head_ptr()
                result, comps = DaatANDwithSkip(h1, h2)
                result_list = result.find_node()
                total_comparisons += comps
            query_dict['num_comparisons'] = total_comparisons
            query_dict['num_docs'] = len(result_list)
            query_dict['results'] = result_list
            
            d[og[z]] = query_dict
            z += 1
        main_d['daatAndSkip'] = d

    elif flag == 3:
        d = {}
        z = 0
        for query in list_of_term_postings:
            query_dict = {}
            total_comparisons = 0
            result_dict = {}
            result_list = []
            for i in range(len(query) - 1):
                h1 = query[i]['postings_list'].get_head_ptr()
                h2 = query[i + 1]['postings_list'].get_head_ptr()
                result, comps = DaatAND(h1, h2)
                result_dict = result.find_node_tfidf()
                result_dict = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
                for k, v in result_dict.items():
                    result_list.append(k)
                total_comparisons += comps
            query_dict['num_comparisons'] = total_comparisons
            query_dict['num_docs'] = len(result_list)
            query_dict['results'] = result_list
            
            d[og[z]] = query_dict
            z += 1
        main_d['daatAndTfIdf'] = d

    else:
        d = {}
        z = 0
        for query in list_of_term_postings:
            query_dict = {}
            total_comparisons = 0
            result_dict = {}
            result_list = []
            for i in range(len(query) - 1):
                h1 = query[i]['postings_list'].get_head_ptr()
                h2 = query[i + 1]['postings_list'].get_head_ptr()
                result, comps = DaatANDwithSkip(h1, h2)
                result_dict = result.find_node_tfidf()
                result_dict = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
                for k, v in result_dict.items():
                    result_list.append(k)
                total_comparisons += comps
            query_dict['num_comparisons'] = total_comparisons
            query_dict['num_docs'] = len(result_list)
            query_dict['results'] = result_list
            
            d[og[z]] = query_dict
            z += 1
        main_d['daatAndSkipTfIdf'] = d
        print(json.dumps(main_d))
        return(main_d)