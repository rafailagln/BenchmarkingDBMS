import re
import vertica_sdk


# --------------------- BEGIN EXTRACT IP ---------------------
class extract_ip(vertica_sdk.ScalarFunction):

    """
    Extract ip from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting ip - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r"(^\S+) ", logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass


class extract_ip_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_ip()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(15)
# ---------------------- END EXTRACT IP ----------------------


# --------------------- BEGIN EXTRACT CLIENT ID ---------------------
class extract_client_id(vertica_sdk.ScalarFunction):

    """
    Extract client id from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting client id - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r"^\S+ (\S+) ", logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_client_id_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_client_id()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(8)
# ---------------------- END EXTRACT CLIENT ID ----------------------


# --------------------- BEGIN EXTRACT USER ID ---------------------
class extract_user_id(vertica_sdk.ScalarFunction):

    """
    Extract user id from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting user id - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r"^\S+ \S+ (\S+) ", logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_user_id_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_user_id()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(8)
# ---------------------- END EXTRACT USER ID ----------------------


# --------------------- BEGIN EXTRACT DATE ---------------------
class extract_date(vertica_sdk.ScalarFunction):

    """
    Extract date from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting date - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r"^.*\[([\w:/]+\s[+\-]\d{4})\]", logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_date_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_date()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(27)
# ---------------------- END EXTRACT DATE ----------------------


# --------------------- BEGIN EXTRACT METHOD ---------------------
class extract_method(vertica_sdk.ScalarFunction):

    """
    Extract method from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting method - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r'^.*"(\S+) \S+\s*\S*\s*"', logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_method_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_method()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(100)
# ---------------------- END EXTRACT METHOD ----------------------


# --------------------- BEGIN EXTRACT ENDPOINT ---------------------
class extract_endpoint(vertica_sdk.ScalarFunction):

    """
    Extract endpoint from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting endpoint - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r'^.*"\S+ (\S+)\s*\S*\s*"', logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_endpoint_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_endpoint()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(150)
# ---------------------- END EXTRACT ENDPOINT ----------------------


# --------------------- BEGIN EXTRACT PROTOCOL ---------------------
class extract_protocol(vertica_sdk.ScalarFunction):

    """
    Extract protocol from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting protocol - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r'^.*"\S+ \S+\s*(\S*)\s*"', logline)
            if match:
                res_writer.setString(match[1])
                res_writer.next()
            else:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_protocol_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_protocol()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(8)
# ---------------------- END EXTRACT PROTOCOL ----------------------


# --------------------- BEGIN EXTRACT RESPONSE CODE ---------------------
class extract_response_code(vertica_sdk.ScalarFunction):

    """
    Extract response code from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting response code - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r'^.*" (\d{3}) ', logline)
            if match:
                res_writer.setInt(int(match[1]))
                res_writer.next()
            else:
                res_writer.setInt(-1)
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_response_code_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_response_code()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
# ---------------------- END EXTRACT RESPONSE CODE ----------------------


# --------------------- BEGIN EXTRACT CONTENT SIZE ---------------------
class extract_content_size(vertica_sdk.ScalarFunction):

    """
    Extract content size from apache server log
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting content size - UDx")

        while(True):
            logline = arg_reader.getString(0)
            match = re.search(r'^.*" \d{3} (\S+)', logline)
            if match:
                res_writer.setInt(0 if match[1] == '-' else int(match[1]))
                res_writer.next()
            else:
                res_writer.setInt(-1)
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extract_content_size_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extract_content_size()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
# ---------------------- END EXTRACT CONTENT SIZE ----------------------