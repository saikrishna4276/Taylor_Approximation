# Taylor Approximation

The following app is based on Taylor Approximation and is built using ```Streamlit```

Given a function, $n^{th}$ degree taylor approximation can be done about point ```a``` (variable).

A degree n can be chosen using slider from 1 to n. (Max value of n is 10)

The app for Taylor approximation of arbitary function about any point can be acceded [here](https://saikrishna4276-taylor-approximation-taylor-arbitaryfn-jke7ay.streamlit.app/)


### NOTE:
1. Make sure the expression are valid, 
    
    valid expressions: sin(x) * cos(x)
    
    Inavalid expressions: sin(x)cos(x)
    
    ![inavlid_expr](./images/invalie_exp.png)

2. You cannot approximate the functions which are not define about ```a```.

For Example:
    $ f(x) = 1/x $ ```at``` $ a = 0 $ is undefined or nan.
    ![undefined](./images/undefined.png)

3. The functions which cause overflow (inf) or undeflow (-inf) are replaced with 10e+6 and 10e-6 respectively. 

Example: $log(x)$ at $a = 0$

![log](./images/large.png)