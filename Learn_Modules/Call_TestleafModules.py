# Way 01
import Learn_Modules.TestleafModules

obj1 = Learn_Modules.TestleafModules.Testleaf01()
obj1.python()
obj1.devOps()

# Way 02
from Learn_Modules.TestleafModules import TestLeaf02
obj2 = TestLeaf02()
obj2.automation()

# Way 03
from Learn_Modules.TestleafModules import TestLeaf03 as t3
x = t3()
x.automation1()

# Way 04
from Learn_Modules.TestleafModules import Testleaf01, TestLeaf02

# Way 05
from Learn_Modules.TestleafModules import TestLeaf03 as t3, TestLeaf02 as t2
