// Decompile every function to <out>/decompiled.c and list imports/strings xrefs.
//@category Warmonger
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import java.io.*;

public class DumpDecomp extends GhidraScript {
    @Override
    public void run() throws Exception {
        String out = getScriptArgs().length > 0 ? getScriptArgs()[0] : "/tmp";
        DecompInterface di = new DecompInterface();
        di.openProgram(currentProgram);
        try (PrintWriter w = new PrintWriter(new FileWriter(out + "/decompiled.c"))) {
            FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
            int n = 0;
            while (it.hasNext() && !monitor.isCancelled()) {
                Function f = it.next();
                if (f.isThunk() || f.isExternal()) continue;
                DecompileResults r = di.decompileFunction(f, 60, monitor);
                w.println("// ==== " + f.getEntryPoint() + " " + f.getName(true));
                if (r != null && r.decompileCompleted()) w.println(r.getDecompiledFunction().getC());
                else w.println("// decompile failed");
                if (++n % 1000 == 0) println("decompiled " + n);
            }
        }
        try (PrintWriter w = new PrintWriter(new FileWriter(out + "/imports.txt"))) {
            for (Symbol s : currentProgram.getSymbolTable().getExternalSymbols()) {
                StringBuilder refs = new StringBuilder();
                for (Reference r : getReferencesTo(s.getAddress())) refs.append(" ").append(r.getFromAddress());
                w.println(s.getParentNamespace().getName() + "!" + s.getName() + refs);
            }
        }
    }
}
