<h2><a href="https://leetcode.com/problems/meeting-rooms">252. Meeting Rooms</a></h2><h3>Easy</h3><hr><p>You are given an array of meeting times&nbsp;<code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>.</p>

<p>A person can attend all meetings if no two meeting intervals overlap. Meetings ending at time <code>t</code> and starting at time <code>t</code> <strong>do not</strong> overlap.</p>

<p>​​​​​​​Return <code>true</code> if a person can attend all meetings. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;&nbsp;end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>
