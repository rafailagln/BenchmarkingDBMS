import vertica_sdk

# --------------------- BEGIN FIX ZIPS ---------------------
class fix_zip_codes(vertica_sdk.ScalarFunction):

    """
    Fix zip codes
    """

    def __init__(self):
        pass

    def setup(self, server_interface, col_types):
        pass

    def processBlock(self, server_interface, arg_reader, res_writer):
        # Writes a string to the UDx log file.
        server_interface.log("Fixing zipcode - UDx")

        while(True):
            zips = arg_reader.getString(0)
            if not zips:
                res_writer.setString(None)
                res_writer.next()
            # Truncate everything to length 5
            s = zips[:5]

            # Set 00000 zip codes to nan
            if s == "00000":
                res_writer.setString(None)
                res_writer.next()
            else:
                res_writer.setString(s)
                res_writer.next()

            if not arg_reader.next():
                # Stop processing when there are no more input rows.
                break

    def destroy(self, server_interface, col_types):
        pass
            

class fix_zip_codes_factory(vertica_sdk.ScalarFunctionFactory):
    def createScalarFunction(self, srv):
        return fix_zip_codes()

    def getPrototype(self, srv_interface, arg_types, return_type):
        arg_types.addVarchar()
        return_type.addChar()

    def getReturnType(self, srv_interface, arg_types, return_type):
        return_type.addChar(5)
# ---------------------- END FIX ZIPS ----------------------