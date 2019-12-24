# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# sets a variable with the package's internal name
package = 'app.buzz.share'

# sets a variable with the name of an Activity in the package
activity = 'com.ss.android.buzz.BuzzMainActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)

# MonkeyRunner.sleep(5)
# activity = 'com.bytedance.polaris.browser.PolarisBrowserActivity'
# runComponent = package + '/' + activity
# device.startActivity(component=runComponent)

