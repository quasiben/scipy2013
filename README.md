SciPy 2013 Data Processing Tutorial
====

##Recap

Thank you to everyone for coming to our tutorial. We hope you all learned something new and useful, and encourage everyone to continue the lively discussions from the sessions throughout this week and beyond. Towards that aim of facilitating further discussion of these topics, here is a quick rundown of the topics we went over and some additional resources for those interested in learning more.

* The [tutorial GitHub repo](https://github.com/quasiben/scipy2013) contains the slides and exercises, and should stay up for a while.
* Your demo accounts on [Wakari.io](https://wakari.io) are not permanent, but it's super easy to sign up for a free account. Wakari is in active development, so if there's a feature you want or an annoyance you don't, feel free to [give us a shout](wakari_support@continuum.io)!

## Pandas

* Series and DataFrame extend NumPy to enable more expressive data processing.
* Indices are optional, but allow features like selection of date ranges. 
* Handles missing data well, provided you tell it what missing data looks like with `na_values`.
* Resampling and reindexing are powerful. Learn them, love them.
* **Exercises:**
    * Demo 1: Series
    * Demo 2: DataFrame
    * Exercise: Continous Glucose Monitor Data
        * Solutions in "Solutions" folder
* **Recommended text:** [Python for Data Analysis, by Wes McKinney](http://shop.oreilly.com/product/0636920023784.do).

## IPCluster

* IPCluster clients talk to a central controller, which in turn wrangles remote nodes, each running one or more engines.
* An engine is like a thread. You can run an engine on the same node as a controller, and nodes can run more than one engine. 
* Configuration is flexible, but somewhat poorly documented. For development, run `ipcluster start -n 3` to start three engines, and connect to them from IPython with

        from IPython.parallel import Client
        client = Client()
* Execute commands with view methods e.g. `direct.execute('foo()')` **not** `client.execute('foo()')`.
* IPCluster is ideal for embarassingly parallel workloads that are CPU/GPU/RAM-heavy and light on data transfer.
* **Exercise:** IPCluster Basics
* **Exercise:** Bayesian Estimation w/ MCMC and IPCluster ([view/clone this notebook with Wakari](https://www.wakari.io/sharing/bundle/clayadavis/ipcluster_mcmc)).
* **Recommended notebook:** [Introduction to Parallel Python with IPCluster and Wakari](https://www.wakari.io/sharing/bundle/ijstokes/ipcluster-wakari-intro), Ian Stokes-Rees.
* **Recommended text:** [Doing Bayesian Data Analysis](http://www.indiana.edu/~kruschke/DoingBayesianDataAnalysis/), John K Kruschke.

## MapReduce

* Good for data-heavy workloads that can be implemented as a set of filters (map) and aggregators (reduce).
* Can generate large amounts of network traffic.
* Obligatory SQL analogy of a MapReduce job:
    * Map step filters data (SELECT BY ...), outputs key/value pair (SQL GROUP BY key).
    * Partitioning sends k/v pairs such that all pairs with similar key go to same reduce node.
    * Reduce step performs the aggregate function (COUNT, SUM, GROUP CONCAT) on all values with the same key.
* MapReduce as a concept is separate from its implementations. Popular implementations include Disco and Hadoop.
* **Exercise:** Bitly data from `.gov` and `.mil`
* **Exercise:** WikiLogs
* **Recommended blogposts:** [Map/Reduce – A visual explanation](http://ayende.com/blog/4435/map-reduce-a-visual-explanation), and its follow-up [What is map/reduce for, anyway?](http://ayende.com/blog/4436/what-is-map-reduce-for-anyway) by Ayende Rahien.
* **Recommended reading:** [MapReduce: Simplified Data Processing on Large Clusters](www.usenix.org/event/osdi04/tech/full_papers/dean/dean.pdf) by Jeffrey Dean and Sanjay Ghemawat.

## Data Exploration
### (Unsupervised machine learning)

* Principal Component Analysis (PCA) and Singular Value Decomposition (SVD) find the axes with highest variance.
    * These high variance axes represent the "important" variables.
    * Implementations in Numpu/Scipy and SciKits-Learn
* K-means clustering tries to group "similar" data points together.
    * The number of clusters K is an input parameter. This is good or bad depending on the problem.
    * Methods like Bayesian Information Content can help determine K from the data if it is unknown.
* **Exercises:** K-means and PCA clustering.
