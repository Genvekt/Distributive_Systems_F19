# Lab 9: Replication and Sharding
### Before the deletion of primary data node:
#####  Simple Web Chat Application Screenshot:
![Screenshot](https://raw.githubusercontent.com/Genvekt/Distributive_Systems_F19/master/Lab9/Screenshot%20from%202019-10-29%2016-19-47.png)
##### rs.status() output:

```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-29T16:27:08.610Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572366420, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-10-29T16:27:00.945Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572366420, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-29T16:27:00.945Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572366420, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572366420, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-10-29T16:27:00.945Z"),
		"lastDurableWallTime" : ISODate("2019-10-29T16:27:00.945Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572366390, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572366390, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-10-29T14:13:29.698Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572358398, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-29T14:13:30.722Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T14:13:31.605Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1:27017",
			"ip" : "172.31.32.57",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 8093,
			"optime" : {
				"ts" : Timestamp(1572366420, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-29T16:27:00Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572358409, 1),
			"electionDate" : ISODate("2019-10-29T14:13:29Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "db2:27017",
			"ip" : "172.31.82.163",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 8029,
			"optime" : {
				"ts" : Timestamp(1572366420, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572366420, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-29T16:27:00Z"),
			"optimeDurableDate" : ISODate("2019-10-29T16:27:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T16:27:08.157Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T16:27:07.813Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db1:27017",
			"syncSourceHost" : "db1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "db3:27017",
			"ip" : "172.31.91.67",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 8029,
			"optime" : {
				"ts" : Timestamp(1572366420, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572366420, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-29T16:27:00Z"),
			"optimeDurableDate" : ISODate("2019-10-29T16:27:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T16:27:08.217Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T16:27:07.903Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db1:27017",
			"syncSourceHost" : "db1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572366420, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572366420, 1)
}
```
##### rs.config() output:
```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "db1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "db2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "db3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db848fed2529cfa607eac4a")
	}
}

```

### After the deletion of primary data node:
#####  Simple Web Chat Application Screenshot:
![Screenshot](https://raw.githubusercontent.com/Genvekt/Distributive_Systems_F19/master/Lab9/Screenshot%20from%202019-10-29%2016-52-26.png)
##### rs.status() output:
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-29T16:41:29.824Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572367286, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-10-29T16:41:26.962Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572367286, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-29T16:41:26.962Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572367286, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572367286, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-10-29T16:41:26.962Z"),
		"lastDurableWallTime" : ISODate("2019-10-29T16:41:26.962Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572367236, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572367236, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-29T16:40:26.577Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572367220, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572367220, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(0),
		"newTermStartDate" : ISODate("2019-10-29T16:40:26.960Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T16:40:28.043Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1:27017",
			"ip" : "172.31.32.57",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T16:41:26.585Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T16:40:26.561Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "db2:27017",
			"ip" : "172.31.82.163",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 9409,
			"optime" : {
				"ts" : Timestamp(1572367286, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-29T16:41:26Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572367226, 1),
			"electionDate" : ISODate("2019-10-29T16:40:26Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "db3:27017",
			"ip" : "172.31.91.67",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 8890,
			"optime" : {
				"ts" : Timestamp(1572367286, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572367286, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-29T16:41:26Z"),
			"optimeDurableDate" : ISODate("2019-10-29T16:41:26Z"),
			"lastHeartbeat" : ISODate("2019-10-29T16:41:28.608Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T16:41:28.051Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db2:27017",
			"syncSourceHost" : "db2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572367286, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572367286, 1)
}

```
##### rs.config() output:
```
rs0:PRIMARY> rs.conf()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "db1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "db2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "db3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db848fed2529cfa607eac4a")
	}
}

```
