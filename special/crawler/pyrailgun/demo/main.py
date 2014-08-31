from pyrailgun import RailGun

railgun = RailGun()
railgun.setTask(file("testsite.json"));
railgun.fire();
# nodes = railgun.getShells('default')
# print nodes