import math
import re
import vertica_sdk

# --------------------- BEGIN EXTRACT BEDROOMS ---------------------
class extractbd(vertica_sdk.ScalarFunction):

    """
    Extract bedrooms
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting bedrooms - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                max_idx = val.find(' bd')
                if max_idx < 0:
                    max_idx = len(val)
                s = val[:max_idx]
                split_idx = s.rfind(',')
                if split_idx < 0:
                    split_idx = 0
                else:
                    split_idx += 2
                r = s[split_idx:]
                res_writer.setInt(int(r))
                res_writer.next()
            except:
                res_writer.setInt(-1)
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extractbd_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extractbd()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
# ---------------------- END EXTRACT BEDROOMS ----------------------



# --------------------- BEGIN EXTRACT BATHROOMS ---------------------
class extractba(vertica_sdk.ScalarFunction):

    """
    Extract bathrooms
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting bathrooms - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                max_idx = val.find(' ba')
                if max_idx < 0:
                    max_idx = len(val)
                s = val[:max_idx]
                split_idx = s.rfind(',')
                if split_idx < 0:
                    split_idx = 0
                else:
                    split_idx += 2
                r = s[split_idx:]
                ba = math.ceil(2.0 * float(r)) / 2.0
                res_writer.setInt(int(ba))
                res_writer.next()
            except:
                res_writer.setInt(-1)
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extractba_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extractba()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
# ---------------------- END EXTRACT BATHROOMS ----------------------



# --------------------- BEGIN EXTRACT SQFEET ---------------------
class extractsqfeet(vertica_sdk.ScalarFunction):

    """
    Extract square feet
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting square feet - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                max_idx = val.find(' sqft')
                if max_idx < 0:
                    max_idx = len(val)
                s = val[:max_idx]
                split_idx = s.rfind('ba ,')
                if split_idx < 0:
                    split_idx = 0
                else:
                    split_idx += 5
                r = s[split_idx:]
                r = r.replace(',', '')
                res_writer.setInt(int(r))
                res_writer.next()
            except:
                res_writer.setInt(-1)
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extractsqfeet_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extractsqfeet()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
# ---------------------- END EXTRACT SQFEET ----------------------



# --------------------- BEGIN EXTRACT PRICE SELL ---------------------
class extractprice_sell(vertica_sdk.ScalarFunction):

    """
    Extract price sell
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting price sell - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                res_writer.setInt(int(val[1:].replace(',', '')))
                res_writer.next()
            except:
                res_writer.setInt(-1)
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extractprice_sell_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extractprice_sell()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addInt()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addInt()
# ---------------------- END EXTRACT PRICE SELL ----------------------



# --------------------- BEGIN EXTRACT ID ---------------------
class extractid(vertica_sdk.ScalarFunction):

    """
    Extract id
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting id - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                match = re.search("(\d+)_zpid/$",val)
                res_writer.setString(match.group(1))
                res_writer.next()
            except:
                res_writer.setString('-1')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extractid_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extractid()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(10)
# ---------------------- END EXTRACT ID ----------------------



# --------------------- BEGIN EXTRACT PCODE ---------------------
class extractpcode(vertica_sdk.ScalarFunction):

    """
    Extract postal code
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting postal code - UDx")

        while(True):
            val = arg_reader.getInt(0)
            try:
                res_writer.setString('%05d' % val)
                res_writer.next()
            except:
                res_writer.setString('')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extractpcode_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extractpcode()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addInt()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(10)
# ---------------------- END EXTRACT PCODE ----------------------



# --------------------- BEGIN EXTRACT TYPE ---------------------
class extracttype(vertica_sdk.ScalarFunction):

    """
    Extract type
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Extracting type - UDx")

        while(True):
            val = arg_reader.getString(0)
            try:
                t = val.lower()
                type = 'unknown'
                if 'condo' in t or 'apartment' in t:
                    type = 'condo'
                if 'house' in t:
                    type = 'house'
                res_writer.setString(type)
                res_writer.next()
            except:
                res_writer.setString('-1')
                res_writer.next()
            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class extracttype_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return extracttype()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(10)
# ---------------------- END EXTRACT TYPE ----------------------