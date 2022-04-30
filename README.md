To check two configurations:
   - from ConfigTree import Configtree
   - run ConfigTree.isSame(config1,config2) where config1 and config2 are contents of Aerospike configuration files.
   - If isSame() returns true then only both configurations are same otherwise different and should be made same.

If both configurations are not same then pass the roots of both trees to makCorrectConfig() function with the master config root as the first arg.

makeCorrecConfig() will then return the correct config to be used.

To create the config string from the correct ConfigTree, call stringify(root) where root is the root of the correct ConfigTree.