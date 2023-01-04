import string
import vertica_sdk

def to_lower(val):
    return val.lower()

def strip(val):
    return val.strip()

def replace_o_a(val):
    return val.replace('o', 'a')
    
    
# --------------------- BEGIN LOWER ---------------------
class to_lower(vertica_sdk.ScalarFunction):

    """
    Extract content size from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Validating webpage accessibility - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                r = val.lower()
                res_writer.setString(r)
                res_writer.next()
            except:
                res_writer.setString('-1')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class to_lower_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return to_lower()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(100)
# ---------------------- END LOWER ----------------------


# --------------------- BEGIN STRIP ---------------------
class to_strip(vertica_sdk.ScalarFunction):

    """
    Extract content size from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Validating webpage accessibility - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                r = val.lower()
                res_writer.setString(r)
                res_writer.next()
            except:
                res_writer.setString('-1')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class to_strip_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return to_strip()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(100)
# ---------------------- END STRIP ----------------------


# --------------------- BEGIN REPLACE O A ---------------------
class replace_o_a(vertica_sdk.ScalarFunction):

    """
    Extract content size from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Validating webpage accessibility - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                r = val.replace('o', 'a')
                res_writer.setString(r)
                res_writer.next()
            except:
                res_writer.setString('-1')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class replace_o_a_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return replace_o_a()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(100)
# ---------------------- END REPLACE O A ----------------------