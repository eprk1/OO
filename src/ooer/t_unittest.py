from unittest.mock import MagicMock


class ProductionClass:
    def foo(self):
        return 5

    def bar(self):
        self.cmd("something")
        return self.foo() * 2

    def cmd(self, cmd):
        return


thing = ProductionClass()
thing.foo = MagicMock(return_value=3)
thing.cmd = MagicMock(return_value=True)

print(thing.bar())
thing.cmd.assert_called_once()

print(thing.cmd.call_args.kwargs)
print(thing.cmd.call_args.args)
print(thing.cmd.call_args_list)

if "some" in thing.cmd.called_args.args:
    print("YEAH")
else:
    print("NO")


print(ProductionClass().bar())


"""
    @unittest.skipIf(sys.version_info.major < 3,
                   "Python 2 devtools does not build Python 3 wheels")
    def test_BuildStep_execute(self):
        from unittest.mock import MagicMock
        test_obj = bld.BuildStep(tempfile.gettempdir())
        test_obj.is_btype_release = MagicMock(return_value=True)
        test_obj.run_cmd_wrapper = MagicMock(return_value=True)
        test_obj.execute()
"""
