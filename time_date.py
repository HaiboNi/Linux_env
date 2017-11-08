###
#  time date plugin used in sublime text to record time of change,
#  add key binding by :
#  adding: { "keys": ["f5"], "command": "insert_datetime"} 
#  to user defined key bindings.
#
####



import sublime, sublime_plugin, time
class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel();


        now_time = time.localtime()

        now_time_out = '%s:%02d:%02d, %s, %02d-%s-%04d, By Haibo'% (now_time.tm_hour,now_time.tm_min,now_time.tm_sec,  \
        			  time.strftime('%a'),  now_time.tm_mday, time.strftime('%B'), now_time.tm_year )
        for s in sel:
            # self.view.replace(edit, s, '// ' + time.ctime() + ': by Haibo') 
            self.view.replace(edit, s, '// ' + now_time_out)


