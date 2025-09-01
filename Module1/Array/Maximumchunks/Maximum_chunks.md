[https://leetcode.com/problems/max-chunks-to-make-sorted/description/](https://leetcode.com/problems/max-chunks-to-make-sorted/description/)

For this question i took 2 days , firstly i had watched video and not able to understood the code kyuki  mai neend me thi ya smghna ni cha ri ti ya lg rha tha ki yeh i j mughe smgh aa hi ni skta phir subha leetcode pr gemini se solve krkr chap diya phir didi ne interview liya toh problm smgha di code ni smgha payi phir usi din mne video ko dubhara dekha code dekha ni smgh me aya phir gemini ko vo mughe bta isme kya hora h h mai canbechunked function me jo array meri index se compare kri h vo line ni smgh pari ti thi mtlb mughe yeh smgh ni maa para tha ki arr\[k\] jo h vo i or j se com pare isly krega kyuki ek sorted array ka index voi toh hoga jo uska elemnt hoga .  iski 2 approch smghli ek greedy jisme O\[n\*2\] complexity ayi or ek pmax jisme O(n) ayi. 

In maximum chunk approach we have one array and in array we have to perform 3 main function 

1. Splitting into multiple chunks  
2. Sorting that dividing chunks  
3. Concatenate that chunks   
4. And check that we got sorted array or not   
5. Find the maximum number of chunks in this

APPROACH for main function:  
 Approach me sbse phle we have take one array   
Now in that array    
Firstly we have to use one loop i that will go through each element of whole array   
Then we have one inner loop j joki i se lekr N tk jayega yehi vo loop h jisme yeh check krega ki vo chunk possible hai ya ni meand (canbechunked function me check krega ), if its value is TRUE then we add ans=ans+1, and also we with update the value of j jisse aab iterate hoga us chunk ke bad vale element se so i=j+1  
Then after forming one chunk we will break that loop and then iterate for another ith element means inner loop will be break and then while loop that is outer loop will be work again with new updated ith value. And return the value of ans .

Now main function that is canbechunked will be in progress this function will check wether an chunk made is valid or not .  
APPROCH for this : 

Ek loop k chlega i to j tk , this loop will check that element jo i se j tk h vo ek asa group form kra h jisme values jo h vo ek permutation way me h for exampl take an array of \[1,0,2,3,4\] to yeh check krega ki index 0 se 0 tk ek permuation group h ya ni (1,1) agr ni toh check krega index 0 se 1 tk ki permutation group hai ya ni jab milega ki h jse 1,0 elemnt h toh phir yeh ruk jayega or ek chucnk form krega condition used will be arr\[k\]\>=i and arr\[k\] \<=j  Hum isme i or j indecs kyu kreh kyuki kisi bhi sorted array me arr\[i\] ki value i hi toh hogi 0 index pr  0 hi toh hoga or j me bhi same hi use hoga or agr arr\[k\] ki value i or j ke bech me ayi toh mtlb vha tk chu nk ban skta h , then count=count+1  
If count ki value equal hoti h number of element ke then it will be true else it will be false  
Number of elemnt will j-i+1.

So in this as i as seeing there are 2 loops one is outer of while loop and other is for so its time complexity will be O(n\*2).

And we to find maximum number of chunks so we used greedy approach here.

    
class Solution:  
    def maxChunksToSorted(self, arr: List\[int\]) \-\> int:  
        n=len(arr)  
        i=0  
        ans=0  
        while i\<n:  
            for j in range(i,n):  
                if (self.canbechuked(arr,i,j)):  
                    ans=ans+1  
                    i=j+1  
                    break    
        return ans  
    def canbechuked(self, arr: list\[int\], i: int, j: int) \-\> bool:  
        count=0  
        for k in range(i,j+1):  
            if arr\[k\]\>=i and arr\[k\]\<=j:  
                count=count+1  
        if count==(j-i+1):  
            return True  
        else:  
            return False

ALso to optimize this solution we use pmax method also:  
Jse ki hum isme ek pmax array bna nge usse kya hoga ek pmax array bnaye jse for exm \[1,0,3,2\] so pmax array of this will be \[1,1,3,3\] now hum is pmax array ko compare krnge  array ke index ke equal toh mtlb hmara array shi jgha pr h vrna chunk ni homge divide  
Jse \[1,1,3,3\] pmax h toh yeh compare krega array ke index se jse 1 compare kiya index 0 ni h toh abb phir 1 compare krega index 1 se hai toh ek chunk ans+1 , now 3 compare prega index 2 se ni h , 3 compare krega index 3 se h toh vha chunk ans \+1 hoga .

Yeh optimal isly h because time complexity is 0(n) .

class Solution:  
    def maxChunksToSorted(self, arr: List\[int\]) \-\> int:  
        n=len(arr)  
        if len(arr)\<=1:  
            return 1  
        ans=0  
        pmax=\[0\]\*len(arr)  
        pmax\[0\]=arr\[0\]  
        for i in range(1,n):  
            pmax\[i\]=max(pmax\[i-1\],arr\[i\])  
        for i in range(n):  
            if pmax\[i\]==i:  
                ans=ans+1  
         
        return ans

Learning from this problem:  
Remember that every time you struggle, you're building a stronger foundation. The feeling of finally understanding something after a long effort is one of the best parts of learning. Keep pushing through those tough problems\!  
