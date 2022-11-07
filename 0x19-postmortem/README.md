<h1>Postmortem Report</h1> <br>

<h1>Issue Summary</h1><br>
It was reported that the  CalorieMealPlanner platform was returning 500 Error on all requests made on the platform routes, all the services were down. All the users were affected. The root cause was the failure of our master server web-01.

<h1>Timeline (West African Timezone +1)</h1><br>
•	9:45 PM: 500 Server error detected <br>
•	9:46 PM: The pagerduty give a notification to the engineer on standby <br>
•	9:50 PM: Backup/Standby server (web-02) was put in place <br>
•	9:53 PM: Server restart begin <br>
•	9:55 PM: CalorieMealPlanner start working 100% <br>


<h1>Roor=t Cause</h1><br>
The web application(CalorieMealPlanner) platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a results of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards

<h1>Corrective and preventive measure</h1> <br>
Our monitoring systems alerted our engineers at 9:45 PM GMT, and they investigated and quickly escalated the issue. Since we had two servers and one load balancer we configured one of the servers to act as a Load balancer as we plan to acquire new servers and hardware load balancers. The issue was fixed when the master server was temporarily disconnected for memory clean-up then connected back to the loadbalancer and round-robin algorithm was configured so that both the master and client servers can handle equal amount of requests. At 9:53 PM we restarted the new configured load balancer and users could now access the web application(CalorieMealPlanner).

<h1>Corrective and preventive measure</h1> <br>
•	Choose the best loadbalancing algorithm for your programs <br>
•	Always keep an eye on your servers to ensure they are running properly <br>
•	Have extra back-up servers to prevent your program fro completely going offline during an issue <br>
