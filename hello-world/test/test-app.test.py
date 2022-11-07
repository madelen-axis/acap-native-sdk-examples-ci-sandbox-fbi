import os
from logging import log, error, step, is_true

# from nose.plugins.attrib import attr
# from axis_features.nose_plugin import axis_features
# from atf_common.assertions import is_true, error
# from atf_common.logging import step, log
# from dut.manager import DutManager
# from toolbox_utils.toolbox_common import operations_invoker
# from application_library.applications import Applications
    
   
class TestHelloWorld:
    #    """Functional tests for docker containers."""
   
    ACAP_SPECIFIC_NAME = "hello_world"

    @classmethod
    def setup_class(cls):
    #    """Setup class level fixtures.

    #    Class fixtures bracket the execution of everything in the class.
    #    """
        cls.manager = DutManager(dut_address=os.getenv('AXIS_TARGET_ADDR'),
                                username=os.getenv('AXIS_TARGET_USER'),
                                password=os.getenv('AXIS_TARGET_PASS'))
        cls.acap_manager = Applications(cls.manager)
   
    def setup(self):
    #    """Setup class method level fixtures.

    #    Setup class method fixtures.
    #    Bracket the execution of each and every test method in the class.
    #    Function run multiple times, once for each test method.
    #    """
        try:
            self.acap_manager.upload_acap(
                self.get_hello_world_eap_file(), self.ACAP_SPECIFIC_NAME)
        except Exception:
            self.teardown_class()
            raise

    @classmethod
    def teardown_class(cls):
    #    """Teardown class level fixtures.

    #    Class fixtures bracket the execution of everything in the class.
    #    """
        teardown_funcs = [[cls.acap_manager.close],
                            [cls.manager.close]]
        if not operations_invoker(teardown_funcs):
            error("Teardown failed")
   
    def teardown(self):
    #    """Teardown class method level fixtures.

    #    Teardown class method fixtures bracket the execution of each and every test method in the class.
    #    Function run multiple times, once for each test method.
    #    """
        self.acap_manager.stop_acap(self.ACAP_SPECIFIC_NAME)
        self.acap_manager.remove_uploaded_acap(self.ACAP_SPECIFIC_NAME)
        self.manager.restart()
        self.manager.wait_ready()

    @classmethod
    def get_hello_world_eap_file(cls):
    #    """Class method that returns the url to the hello_world application file.

    #    :return: hello_world application url
    #    :rtype: string
    #    """
        with cls.manager.vapix() as vapix:
            arch = str(vapix.param.list("Properties.System.Architecture")).split(
                '=')[1].strip()
            path = os.getenv('WORKSPACE')
            acap_file = os.path.join(
                path, "hello-world/build/hello_world_1_0_0_{}.eap".format(arch))
            return acap_file
   
    def start_hello_world(self):
    #    """Class function that starts hello_world and verifies whether it is running or not."""
        self.acap_manager.start_acap(self.ACAP_SPECIFIC_NAME)
        running = self.acap_manager.wait_for_acap_status(
            self.ACAP_SPECIFIC_NAME, ['Running'])
        if not running:
            log("---------------Test FAILED---------------")
            return False

        self.acap_manager.stop_acap(self.ACAP_SPECIFIC_NAME)
        running = self.acap_manager.wait_for_acap_status(
            self.ACAP_SPECIFIC_NAME, ['Stopped'])
        if not running:
            log("---------------Test FAILED---------------")
            return False

        log("---------------Test OK---------------")
        return True
 
    def read_hello_world_log(self):
          """Class method that reads application logs.
  
          :return: Application logs as String
          :rtype: string
          """
          string = ''
          url = 'http://{}/axis-cgi/admin/systemlog.cgi?appname={}'.format(
              self.manager.dut_ip, self.ACAP_SPECIFIC_NAME)
          with self.manager.http() as http:
              http_response = http.get(url)
              string = http_response.read()
          return string
  
    @ attr("EmbeddedSDK", "FFT", "QART")
    @ axis_features("EmbeddedSDK", "ApplicationAPI")
    def test_hello_world_application(self):
        #   """FFT that verifies some basic manifest ACAP3 functionality using hello_world.
  
        #   Approval criteria:
        #       - hello_world shall be running.
        #       - Hello World! shall be output to syslog exactly once.
        #       - It should be possible to remove the hello_world application.
  
        #   Preconditions:
        #       - hello_world application should be installed on camera.
  
        #   Test steps:
        #   1. Start hello_world application.
        #   2. Verify whether hello_world is Running.
        #   3. Verify that Hello World! has been output in the log exactly once.
        #   4. Remove the ACAP.
        #   5. Verify if it is possible to remove the hello_world application..
        #   """
        step("Start hello_world application.")
        is_true(self.acap_manager.start_acap(self.ACAP_SPECIFIC_NAME),
                "Verify whether hello_world is Running.",
                "hello_world application is not Running.")

        logmessage = str(self.read_hello_world_log())
        hello_world_count = logmessage.count('Hello World!')
        is_true(hello_world_count == 1,
                "Verify that Hello World! has been output in the log exactly once.",
                "Hello World! is supposed to be written to the log exactly once. It was written "
                + str(hello_world_count) + " times instead.")
  
        step("Remove the ACAP.")
        self.acap_manager.stop_acap(self.ACAP_SPECIFIC_NAME)
        is_true(self.acap_manager.remove_uploaded_acap(self.ACAP_SPECIFIC_NAME),
                "Verify if it is possible to remove the hello_world application.",
                "The hello_world application could not be removed.")