'''
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
'''

def method(inputs1,inputs2):
    inputs = zip(inputs1,inputs2)
    res = []
    store = {}
    for _,input2 in inputs:
        if len(input2) == 3:
            timestamp = input2[2]
            store[timestamp] = input2
            res.append('%%')
        elif len(input2) == 2:
            time2 = input2[1]
            if time2 < min(store.keys()):
                res.append('&&')
            elif time2 == min(store.keys()):
                res.append(store[time2][1])
            else:
                left = min(store.keys())
                right = max(store.keys())
                if time2 >= right:
                    res.append(store[right][1])
                else:
                    while time2 > left:
                        time2 -=1
                        if time2 in store.keys():
                            res.append(store[time2][1])
        else:
            res.append('null')
    print(res)

input1 = ["TimeMap","set","set","get","get","get","get","get"]
inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
print(method(input1,inputs))










